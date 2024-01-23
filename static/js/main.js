document.addEventListener('DOMContentLoaded', function () {
    const booksview_el = document.getElementById('booksview')
    const booksview_btn = document.getElementById('booksview_btn')

    booksview_btn.addEventListener('click', addbook)

    function addbook() {
        booksview_el.innerHTML = `
            <h1>Add new Book</h1>
    
            <form class="wrapper align-items-stretch" style="padding: 25px 25px; font-size: 25px;" action="/" method="POST">
                <label for="title">Title:</label>
                <input style="width: 75%; margin: 25px 10px" type="text" name="title" required>
    
                <br style="margin-top: 50px;" />
    
                <label for="author">Author:</label>
                <input style="width: 70%; margin: 25px 10px" type="text" name="author" required>
    
                <br>
    
                <input class="btn btn-success" type="submit" value="Submit">
            </form>
        `
        booksview_btn.innerHTML = `
        <a href="/">Back</a>
        `
    }
})


document.addEventListener('DOMContentLoaded', function () {
    const membersview_el = document.getElementById('membersview')
    const membersview_btn = document.getElementById('membersview_btn')

    membersview_btn.addEventListener('click', addmember)

    function addmember() {
        membersview_el.innerHTML = `
            <h1>Add new Member</h1>
    
            <form class="wrapper align-items-stretch" style="padding: 25px 25px; font-size: 25px;" action="/members" method="POST">
                <label for="name">Name:</label>
                <input style="width: 70%; margin: 25px 10px" type="text" name="name" required>
    
                <br style="margin-top: 50px;" />
    
                <input class="btn btn-success" type="submit" value="Submit">
            </form>
        `
        membersview_btn.innerHTML = `
        <a href="/members">Back</a>
        `
    }
})


document.addEventListener('DOMContentLoaded', function () {
    const transactionsview_el = document.getElementById('transactionsview')
    const transactionsview_btn = document.getElementById('transactionsview_btn')

    transactionsview_btn.addEventListener('click', leasebook)

    function leasebook() {
        transactionsview_el.innerHTML = `
            <h1>Lease a book</h1>
    
            <form class="wrapper align-items-stretch" style="padding: 25px 25px; font-size: 25px;" action="/transactions" method="POST">
                <label for="member_id">Member ID:</label>
                <input style="width: 50%; margin: 25px 10px" type="text" name="member_id" required>
    
                <br style="margin-top: 50px;" />

                <label for="book_id">Book ID:</label>
                <input style="width: 50%; margin: 25px 10px" type="text" name="book_id" required>
    
                <br>
    
                <input class="btn btn-success" type="submit" value="Submit">
            </form>
        `
        transactionsview_btn.innerHTML = `
        <a href="/transactions">Back</a>
        `
    }
})

function removeButtons() {
    buttons = document.querySelectorAll('.btn')
    buttons.forEach((button) => {
        button.remove()
    })
}

function reloadPage() {
    location.reload()
}

function printandReload() {
    removeButtons()
    window.addEventListener('afterprint', reloadPage)
    window.print()
}