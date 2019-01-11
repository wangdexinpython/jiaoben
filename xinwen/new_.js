

// function __doPostBack(eventTarget, eventArgument) {
//     if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
//         theForm.__EVENTTARGET.value = eventTarget;
//         theForm.__EVENTARGUMENT.value = eventArgument;
//         theForm.submit();
//     }
// }

// javascript:__doPostBack('AspNetPager1','3')

function __doPostBack(AspNetPager1,'3') {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
