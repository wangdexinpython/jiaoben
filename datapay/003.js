
var inquirer = require('inquirer')
inquirer.prompt([ {
    type: 'input',
    name: '页码',
    message: '请输入页码：',
    default: 1
}]).then((answers) => { console.log('结果为:')
    console.log(answers)})
