var child_process = require('child_process');

// ruleid: child-process
child_process.exec(cmd);

// ok: child-process
child_process.exec("ls");

const { exec } = require('child_process');

// ruleid: child-process
exec(cmd);

// ok: child-process
exec("ls");

const f = require('child_process').exec;
// ruleid: child-process
f(cmd);

// ok: child-process
f("ls");

const g = require('child_process').fork;
// ok: child-process
g(cmd);
