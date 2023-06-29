// ==UserScript==
// @name         sms-activate.org
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       SamZhou
// @match        https://sms-activate.org/
// @match        https://sms-activate.org/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=sms-activate.org
// @grant        none
// @require      http://libs.baidu.com/jquery/2.0.0/jquery.min.js
// ==/UserScript==

(function () {
    'use strict';
    const POST_URL = "http://127.0.0.1:6789/sms";
    let curr_count = 0;
    let $ = jQuery.noConflict(true);
    let temp = setInterval(() => {
        let div = $('.desktop-grid > div > div > div');
        let phone_number = div.eq(2).text().trim();
        if (div.length <= 0 || phone_number == '') {
            return console.log('not data ...');
        }
        let time = div.eq(3).text().trim();
        let price = div.eq(4).text().trim();
        let msg = div.eq(5).text().trim();
        console.log(phone_number);
        console.log(time);
        console.log(price);
        console.log(msg);

        $.post(POST_URL, { phone_number, time, price, msg }, function (data, status) {
            console.log(data, status)
        })

        if (curr_count >= 1000) {
            clearInterval(temp);
        }
        curr_count++;
    }, 1000 * 3);
})();