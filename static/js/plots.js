// Pull in the data that we want
fetch("/mushrooms")
    .then(res => res.json())
    .then(data => myPlot(data))

function myPlot(data) {
    let mushroom_data = data;
    const total_mushrooms = Object.keys(mushroom_data).length;
    // const poison_mushrooms = Object.keys(mushroom_data === 'p').length;
    let counter_poison = 0;
    for (let i = 0; i<mushroom_data.length;i++) {
        if (mushroom_data[i].poisonous_or_edible === 'p') counter_poison++;
    }
    let counter_edible = 0;
    for (let i = 0; i<mushroom_data.length;i++) {
        if (mushroom_data[i].poisonous_or_edible === 'e') counter_edible++;
    }

    const pie_data = [{
        labels: ["Edible", "Poisonous"],
        values: [counter_edible, counter_poison],
        type: 'pie'
    }];
    
    // console.log(pie_data)
    
    const pie_layout = {
        title: "Poisonous vs Edible Distribution in the Mushroom Data",
    };
    
    // console.log(pie_layout)
    
    return Plotly.newPlot("pie", pie_data, pie_layout)
    }

