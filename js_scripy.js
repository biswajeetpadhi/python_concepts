const { PythonShell } = require('python-shell');

PythonShell.run('D:/python/pythonProject/python_script.py', null, function (err, result) {
  if (err) throw err;
  console.log('Python script executed successfully.');
  console.log('Result:', result);
});
