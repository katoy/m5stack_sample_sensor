
## See https://gist.github.com/dtchepak/13b53eef9dc6b65ae1ad
##
require 'webrick'

class Echo < WEBrick::HTTPServlet::AbstractServlet
  def do_GET(request, response)
    puts request
    response.status = 200
  end

  def do_POST(request, response)
    puts request.header
    puts request
    response.status = 200
  end
end

server = WEBrick::HTTPServer.new(Port: 8080)
server.mount('/', Echo)
trap('INT') { server.shutdown }
server.start

###
# $ ruby http_server.rb
# 
# 別のコンソールから
# $ curl http://localhost:8080/name=123?age=10
# $ curl -X POST -H "Content-Type: application/json" -d '{"Name":"sensuikan1973", "Age":"100"}' localhost:8080
# 
# http_server を起動したコンソールに リクエスト内容が表示される。
