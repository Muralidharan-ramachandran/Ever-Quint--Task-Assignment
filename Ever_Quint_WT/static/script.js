function computeWater() {
    const input = document.getElementById("arrayInput").value;
    const heights = input.split(",").map(x => parseInt(x.trim()));

    fetch("/compute", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ heights })
    })
    .then(res => res.json())
    .then(data => {
        drawGrid(data.heights, data.water, data.total_water);
    });
}

function drawGrid(heights, water, total_water) {

    const maxH = Math.max(...heights.map((h, i) => h + water[i]));

    document.getElementById("result").innerHTML = 
        `Total Water: <b>${total_water}</b> units`;

    let table = "<table>";

    for (let row = maxH; row > 0; row--) {
        table += "<tr>";

        for (let col = 0; col < heights.length; col++) {
            if (row <= heights[col]) {
                table += `<td class="block"></td>`;
            } else if (row <= heights[col] + water[col]) {
                table += `<td class="water"></td>`;
            } else {
                table += `<td></td>`;
            }
        }

        table += "</tr>";
    }

    table += "</table>";

    document.getElementById("grid").innerHTML = table;
}
