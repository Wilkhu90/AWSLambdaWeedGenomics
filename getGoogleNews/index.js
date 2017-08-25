'use strict';
var childProcess = require('child_process');

console.log('Loading function');

exports.handler = (event, context, callback) => {
    childProcess.execFile('curl', ['https://news.google.com/?output=rss&q=herbicide'], function(err, stdout, stderr){
        //console.log(stdout);
        var html = stdout;
        callback(null, html);
    });
};
