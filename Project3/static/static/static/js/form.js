var inputName = d3.select("#inputName").node().value



var svg2 = d3.select("#button")

svg2.on("click", function(d) 
        { 
          console.log(inputName)
        });