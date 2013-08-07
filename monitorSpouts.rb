#!/usr/bin/env ruby
require "zookeeper"
require "kafka"
require "json"
require "optparse"
def config
  ops = {
    :zkhost => "localhost",
    :zkport => 2181,
    :zkpath => "/",
    :topic => nil,
    :outfile => "./spouts.out"
  }
  option_parser = OptionParser.new do |opts|
    opts.banner = './monitorSpouts.rb -h zkhost --port zkport --path zkpath --topic topic'
    opts.on("-h ZKHOST","--host ZKHOST","zookeeper host") { |s|
      ops[:zkhost] = s
    }
    opts.on("--port ZKPORT","zookeeper port") {|s|
      ops[:zkport] = s
    }
    opts.on("--path ZKPATH","zookeeper path") {|s|
      ops[:zkpath] = s
    }
    opts.on("--topic TOPIC","topic") {|s|
      ops[:topic] = s
    }
    opts.on("--outfile outfile","result file") {|s|
      ops[:outfile] = s
    }
  end.parse!
  return ops
end

class MonitorSpouts
  def initialize(options ={})
    @zc = Zookeeper.new("#{options[:zkhost]}:#{options[:zkport]}")
    @zkpath = options[:zkpath]
    @topic = options[:topic]
    @outfile = options[:outfile]
  end
  def monitor
    spouts = @zc.get_children(:path => "#{@zkpath}")[:children]
    num = 0
    fd = File.new(@outfile,"w")
    spouts.each do |spout|
      data = JSON.parse(@zc.get(:path => "#{@zkpath}/#{spout}")[:data])
      if data["topology"]["name"] == @topic
        topic = data["topic"]
        kc = Kafka::Consumer.new({:topic => topic,:host => data["broker"]["host"],:port => data["broker"]["port"]})
        latest = kc.fetch_latest_offset
        current = data["offset"]
        delta = (latest - current)/ 1024
        fd.puts "#{topic}_spout#{num} : #{delta}"
        num += 1
      end
    end
    fd.close
  end
end 

ms = MonitorSpouts.new(config)
ms.monitor
