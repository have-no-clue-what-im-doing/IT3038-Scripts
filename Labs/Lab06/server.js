var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

function formatUptime(uptime) {
    var days = Math.floor(uptime / 86400);
    var hours = Math.floor((uptime % 86400) / 3600);
    var minutes = Math.floor((uptime % 3600) / 60);
    var seconds = Math.floor(uptime % 60);

    return `Days: ${days}, Hours: ${hours}, Minutes: ${minutes},Seconds: ${seconds}`;
}

http.createServer(function(req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body) {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end(body);
        });
    } else if (req.url.match("/sysinfo")) {
        var myHostName = os.hostname();
        var uptime = os.uptime();
        var totalMemory = os.totalmem();
        var freeMemory = os.freemem();
        var cpus = os.cpus();

        
        var uptimeString = formatUptime(uptime);

        var html = `
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${uptimeString}</p>
            <p>Total Memory: ${totalMemory / (1024 * 1024)} MB</p>
            <p>Free Memory: ${freeMemory / (1024 * 1024)} MB</p>
            <p>Number of CPUs: ${cpus.length}</p>            
          </body>
        </html>`;

        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(html);
    } else {
        res.writeHead(404, { "Content-Type": "text/plain" });
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
