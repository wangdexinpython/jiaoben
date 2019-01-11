
// var page_a = require('./page')
//
// // console.log(page_a)
//
// // var pa = 2
//
//
// var mandy_a = require('./mandy')
// var data = mandy_a({'page':page_a, 'pageSize': 10}, "/dynamics/archives", "post");
// console.log(data)


function page() {
    var inquirer = require('inquirer')
inquirer.prompt([ {
    type: 'input',
    name: '页码',
    message: '请输入页码：',
    // default: 1
}]).then((answers) => { console.log('ssssssssss')
    console.log(answers)})


}


function js_mandy() {
    var mandy_a = require('./mandy')

    var data = mandy_a({'page':2,'pageSize':10},"/dynamics/archives","post");

    console.log(data)

}


page()
// js_mandy()
