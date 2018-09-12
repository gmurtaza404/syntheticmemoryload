const fs = require('fs')
const util = require('util')
const http = require('http')

// Promises
const delay = msecs => new Promise(resolve => setTimeout(resolve, msecs))
const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile)

// Globals
let temp_page = "";


const server = http.createServer(async (req,resp) => {
    console.log("serving a request with url" ,req.url)

    let d = ""
    try {
        d = await readFile(req.url.substr(1))
    }catch(err){
        d = "file not found"
    }
    resp.end(d)
})

server.listen(12000, ()=> console.log('Listening'))