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

    // console.log("filter values: ", fvalues);

    // fetch filtered data for prediction
    // Used to filter full database
    // fetch("/mushrooms")
    // .then(res => res.json())
    // .then(data => MLPredict(data))

    // Pass values to predict function
    MLPredict(fvalues)
};

// Variable to hold data for python
let passData;


// feed selected dataset to machine learning and return output
function MLPredict(data) {
    
    // disable submit button until all 4 selections are made
    let c = 0
    for (obj in fvalues) {
        if(fvalues[obj] != undefined) {
            c++
        }
    }

    const button = document.getElementById('ML-button');
    if (c < 4) {
        button.disabled = true;
    }
    else {
        button.disabled = false;
    }

    // Jsonify data for use with machine learning
    // variable to hold updated filter string
    let newStr = ''

    // Iterate through updated options to create data filter
    for (var v = 0; v < Object.keys(fvalues).length; v++) {
        newStr += '"' + Object.keys(fvalues)[v] + '"' + ':"' + Object.values(fvalues)[v] + '",';
    }

    // Drop ending comma from string
    newStr = newStr.slice(0,-1);

    // Add curly braces
    const newFilter = "{" + newStr + "}"
        // console.log(newFilter)

    // pass data to a variable
    const result_dict = JSON.parse(newFilter);
        //console.log(result_dict);
    
    // save data to universal variable for use in sendData()
    passData = result_dict;
        //console.log("passData: " + passData);

// End function
}

let predictText = '';

// pass data to Python for processing
function sendData() {
    fetch("/predict", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        //cache: "no-cache",
        body: JSON.stringify(passData) })
            .then(res => res.json())
            //.then(data => console.log("fetch: " + Object.values(data)))
            .then(data => {
                predictText = Object.values(data);
                //console.log("predictText: " + predictText);
                displayResults();
            });
}

// Update index.html to display the prediction result
let myimg = "";

function displayResults() {
    if (predictText == "edible") {
        myimg = "check.png";
    }
    else {
        myimg = "x.png";
    };

    let v = "<img src='static/images/" + myimg + "' width='30'> &nbsp; <strong>This mushroom is likely to be " + predictText + ".</strong>";
    const txtReplace = document.getElementById("content");
    txtReplace.innerHTML = v;
    //console.log("end of innerHTML: " + predictText);
}
