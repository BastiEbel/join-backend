async function sendMessage() {
    let fd = new FormData();
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;


    fd.append('csrfmiddlewaretoken', token);

    await fetch('/tasks/', {
        method: 'POST',
        body: fd
    });

    console.log('Successfully');
}

function taskDate() {
    moment(newdate).format('YYYY-MM-DD');
}