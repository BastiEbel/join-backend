async function sendMessage(event) {
    event.preventDefault();
    let fd = new FormData();
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;


    fd.append('csrfmiddlewaretoken', token);

    await fetch('', {
        method: 'POST',
        body: fd
    });

    console.log('Successfully');
}

function taskDate() {
    let date = new Date();

    let month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    let days = ('0' + date.getDate()).slice(-2);
    let year = date.getFullYear().toString();

    dateString(date).format(year - month - days);
}