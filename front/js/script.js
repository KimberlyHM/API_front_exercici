
document.addEventListener("DOMContentLoaded", function() {
    // Cridem a l'endpoint de l'API fent un fetch
    fetch("http://127.0.0.1:8000/alumnes/list")
        .then(response => {
            if (!response.ok) {
                throw new Error("Error a la resposta del servidor");
            }
            return response.json();
        })
        .then(data => {
            const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
            alumnesTableBody.innerHTML = ""; // Netejar la taula abans d'afegir res
            
            // Iterar sobre los alumnos y agregarlos al DOM
            data.forEach(alumne => {
                const row = document.createElement("tr");

                // Crear la cel·la per al nom de l'alumne
                const nomAluCell = document.createElement("td");
                nomAluCell.textContent = alumne.NomAlumne;
                row.appendChild(nomAluCell);

                // Crear la cel·la per al cicle
                const cicleCell = document.createElement("td");
                cicleCell.textContent = alumne.Cicle;
                row.appendChild(cicleCell);

                // Crear la cel·la per al curs
                const cursCell = document.createElement("td");
                cursCell.textContent = alumne.Curs;
                row.appendChild(cursCell);

                // Crear la cel·la per al grup
                const grupCell = document.createElement("td");
                grupCell.textContent = alumne.Grup;
                row.appendChild(grupCell);

                // Crear la cel·la per a l'aula (DescAula)
                const aulaCell = document.createElement("td");
                aulaCell.textContent = alumne.DescAula;
                row.appendChild(aulaCell);

                // Añadir la fila completa a la tabla
                alumnesTableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error("Error capturat:", error);
            alert("Error al carregar la llista d'alumnes");
        });
});


