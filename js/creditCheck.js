//exports.creditCheck = function(str) {
exports.creditCheck = function(str) {

    let checkSum = 0;
    let valid = "The number is valid!";
    let invalid = "The number is invalid!";
    newStr = str.split('');

    for (let i = str.length-2; i >= 0; i -= 2) {
        newStr[i] *= 2;
        if (newStr[i] > 9) {
            newStr[i] = newStr[i].toString().split('');
            newStr[i] = (newStr[i][0]*1) + (newStr[i][1]*1)
        }
    }

    newStr.forEach(elem => {
        checkSum += elem * 1;
    })

    return checkSum % 10 === 0 ? valid : invalid
}

//console.log(creditCheck('5541808923795240'))