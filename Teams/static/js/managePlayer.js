(function () {

    const btnRemove = document.querySelectorAll(".btnRemovePlayer");

    btnRemove.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('Are you sure to delete this player?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();