const fs = require('fs');

function readSyncByfs(tips) {
    let response;

    tips = tips || '> ';
    process.stdout.write(tips);
    process.stdin.pause();
    response = fs.readSync(process.stdin.fd, 1000, 0, 'utf8');
    process.stdin.end();
    return response[0].trim();
}

console.log(readSyncByfs('请输入任意字符：'));
