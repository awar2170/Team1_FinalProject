// Pull in the data that we want
fetch("/mushrooms")
    .then(res => res.json())
    .then(data => myPlot(data))

function myPlot(data) {
    let mushroom_data = data;
    console.log(mushroom_data);
}

const pie_data = [{
    labels: ["nonalcoholic beer", "nonalcoholic wine",      "nonalcoholic martini", "nonalcoholic margarita",
"ice tea", "nonalcoholic rum & coke", "nonalcoholic mai tai", "nonalcoholic gin & tonic"],
    values: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
    type: 'pie'
}];

console.log(pie_data)

const pie_layout = {
    title: "'Pie' Chart",
};

console.log(pie_layout)

Plotly.newPlot("pie", pie_data, pie_layout)