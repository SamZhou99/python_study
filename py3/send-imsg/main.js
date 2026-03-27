const exe = require('child_process').exec
const fs = require('fs')


const scriptPath = '../../apple-script/send-msg.scpt'


async function getPhones() {
    let filePath = './phones.txt'
    let phonesText = fs.readFileSync(filePath)
    let phonesArr = phonesText.toString().split('\n')
    return phonesArr
}


async function sendMsg(phoneNum, msgStr) {
    let command = `osascript ${scriptPath} ${phoneNum} '${msgStr}'`
    return new Promise((resolve, reject) => {
        exe(command, (err, stdout, stderr) => {
            if (err) {
                return reject(err)
            }
            return resolve(stdout, stderr)
        })
    })
}


async function init() {
    let phones = await getPhones()
    console.log(phones)
    for (let i = 0; i < phones.length; i++) {
        let phone = phones[i]
        let msgRes = await sendMsg(`+86${phone}`, 'Hello ' + Math.round(Math.random() * 999999))
        console.log(msgRes)
    }
}


init()