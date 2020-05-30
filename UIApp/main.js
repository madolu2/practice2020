let btn = document.querySelector('.btn'),
    response = document.querySelector('#response');

btn.addEventListener('click', () => {
    let fields = Array
        .from(document.querySelectorAll('.form-control'));
    if (fields.filter(input => input.value)) {
        eel.get_fields(fields.map((field) => field.value))(ret => response.innerHTML = ret);
    }
})