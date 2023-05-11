(function () {

  const btnRemove = document.querySelectorAll(".btnRemoveTeam");

  btnRemove.forEach(btn => {
      btn.addEventListener('click', (e) => {
          const confirmacion = confirm('Are you sure to delete this team?');
          if (!confirmacion) {
              e.preventDefault();
          }
      });
  });
  
})();