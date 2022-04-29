// Create a variable to keep track of all the filters as an object.
// Object with Key:Value pairs
const fvalues = {};

// Use this function to update the filters. 
function updateFilters() {

    // Save the element that was changed as a variable.
    const e = d3.select(this);
    //console.log("element: ", e);

    // Save the value that was changed as a variable.
    let filter = e.property("value");
    //console.log("property value: ", filter);

    // Save the id of the filter that was changed as a variable.
    const id = e.attr("id");
    //console.log("id name: ", id);

    // If a filter value was entered then add that filterId and value
    // to the filters list. Otherwise, clear that filter from the filters object.
    if (filter) {
        // removes value from query when option is unselected
        if (filter == '*') {
            delete fvalues[id];
        }
        else {
            fvalues[id] = filter;
        }
    }
    else {
      delete fvalues[id];
    };

    //console.log("filter values: ", fvalues);

    // fetch filtered data for prediction
    fetch("/mushrooms")
        .then(res => res.json())
        .then(data => MLPredict(data))
};

// Variable to hold data for python
let passData;

// feed selected dataset to machine learning and return output
function MLPredict(data) {
    // variablize data
    const myJSON = data;

    // variable to hold updated filter string
    let newStr = ''

    // Iterate through updated options to create data filter
    for (var v = 0; v < Object.keys(fvalues).length; v++) {
        newStr += "el." + Object.keys(fvalues)[v] + " == " + "'" + Object.values(fvalues)[v] + "'" + " && ";
    }

    // Drop ending '&&' text
    newFilter = newStr.slice(0,-3);
        //console.log("New filter string: " + newFilter);

    let filtered = myJSON.filter(function (el) {
        return eval(newFilter);
      });

    // pass data to a variable
    const result_dict = JSON.stringify(filtered);
        //console.log(result_dict);
    passData = result_dict;
      console.log(passData);

    // get count of total result rows
    for (var i = 0; i < filtered.length; i++) {
        // do nothing
    }
    let rcount = i;
        //console.log(rcount);

    // disable submit button if no results
    const button = document.getElementById('ML-button');
    if (rcount < 1) {
        button.disabled = true;
    }
    else {
        button.disabled = false;
    }

    // update query results count display
    const divCount = document.getElementById("rdisplay");
    divCount.innerHTML = "";
    divCount.innerHTML = "&nbsp;Query Results: " + rcount;

    // temporary
    //const divContent = document.getElementById("content");
    //divContent.innerHTML = "";
    //divContent.innerHTML = result_dict;
};


// pass data to Python for processing
function sendData() {
    fetch("/predict", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        //cache: "no-cache",
        body: JSON.stringify(passData) })
            .then(res => res.json())
            // .then(passData => {
            //     console.log('Success:', passData);
            // })
            // .catch((error) => {
            //     console.error('Error:', error);
            // });

            // method: 'POST', // or 'PUT'
            // headers: {
            //     'Content-Type': 'application/json',
            // },
            // body: JSON.stringify(data),

}
