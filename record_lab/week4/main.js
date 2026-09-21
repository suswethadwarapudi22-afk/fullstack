function clearInput() {
    document.getElementById("teamInput").value = "";
}
function showTeam() {

    let team = document.getElementById("teamInput").value;

    if (team == "") {
        team = document.getElementById("teamSelect").value;
    }

    team = team.toLowerCase();

    if (team == "mclaren") {

        document.getElementById("card").innerHTML = `
            <h2>McLaren</h2>
            <p><b>Drivers:</b> Lando Norris, Oscar Piastri</p>
            <p><b>Engine:</b> Mercedes</p>
            <p><b>Position:</b> 3rd</p>
            <p><b>Wins:</b> 1</p>
            <p><b>Points:</b> 220 points</p>
        `;

    }

    else if (team == "ferrari") {

        document.getElementById("card").innerHTML = `
            <h2>Ferrari</h2>
            <p><b>Drivers:</b> Charles Leclerc, Lewis Hamilton</p>
            <p><b>Engine:</b> Ferrari</p>
            <p><b>Position:</b> 2nd</p>
            <p><b>Wins:</b> 2</p>
            <p><b>Points:</b> 307 points</p>
        `;

    }
    else if (team == "mercedes") {

        document.getElementById("card").innerHTML = `
            <h2>Mercedes</h2>
            <p><b>Drivers:</b> George Russell, Kimi Antonelli</p>
            <p><b>Engine:</b> Mercedes</p>
            <p><b>Position:</b> 1st</p>
            <p><b>Wins:</b> 8</p>
            <p><b>Points:</b> 379 points</p>
        `;

    }
    else if (team == "red bull") {

        document.getElementById("card").innerHTML = `
            <h2>Red Bull</h2>
            <p><b>Drivers:</b> Max Verstappen, Isack Hadjar</p>
            <p><b>Engine:</b> Red Bull Ford Powertrains</p>
            <p><b>Position:</b> 4th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 177 points</p>
        `;

    }
    else if (team == "williams") {

        document.getElementById("card").innerHTML = `
            <h2>Williams</h2>
            <p><b>Drivers:</b> Alex Albon, Carlos Sainz</p>
            <p><b>Engine:</b> Mercedes</p>
            <p><b>Position:</b> 9th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 11 points</p>
        `;

    }
    else if (team == "aston martin") {

        document.getElementById("card").innerHTML = `
            <h2>Aston Martin</h2>
            <p><b>Drivers:</b> Fernando Alonso, Lance Stroll</p>
            <p><b>Engine:</b> Honda</p>
            <p><b>Position:</b> 10th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 1 point</p>
        `;

    }
    else if (team == "alpine") {

        document.getElementById("card").innerHTML = `
            <h2>Alpine</h2>
            <p><b>Drivers:</b> Pierre Gasly, Franco Colapinto</p>
            <p><b>Engine:</b> Mercedes</p>
            <p><b>Position:</b> 6th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 61 points</p>
        `;

    }
    else if (team == "haas") {

        document.getElementById("card").innerHTML = `
            <h2>Haas</h2>
            <p><b>Drivers:</b> Esteban Ocon, Oliver Bearman</p>
            <p><b>Engine:</b> Ferrari</p>
            <p><b>Position:</b> 7th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 21 points</p>
        `;

    }
    else if (team == "racing bulls") {

        document.getElementById("card").innerHTML = `
            <h2>Racing Bulls</h2>
            <p><b>Drivers:</b> Arvid Lindblad, Liam Lawson</p>
            <p><b>Engine:</b> Red Bull Ford Powertrains</p>
            <p><b>Position:</b> 5th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 66 points</p>
        `;

    }
    else if (team == "audi") {

        document.getElementById("card").innerHTML = `
            <h2>Audi</h2>
            <p><b>Drivers:</b> Nico Hülkenberg, Gabriel Bortoleto</p>
            <p><b>Engine:</b> Audi</p>
            <p><b>Position:</b> 8th</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b>  12 points</p>
        `;

    }
    else if (team == "cadillac") {

        document.getElementById("card").innerHTML = `
            <h2>Cadillac</h2>
            <p><b>Drivers:</b>Sergio Pérez, Valtteri Bottas</p>
            <p><b>Engine:</b>Ferrari</p>
            <p><b>Position:</b> 22nd</p>
            <p><b>Wins:</b> 0</p>
            <p><b>Points:</b> 0</p>
        `;

     }
    else {

        document.getElementById("card").innerHTML = `
            <h2>Team Not Found</h2>
            <p>Please enter a valid Formula 1 team.</p>
        `;

    }

}