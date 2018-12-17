var width = 960,
    height = 600;

var legendText = ["", "5%", "", "10%", "", "15%", "", "20%"];
var legendColors = ["#fcfbfd", "#efedf5", "#dadaeb", "#bcbddc", "#9e9ac8", "#807dba", "#6a51a3", "#4a1486"];

queue()
    .defer(d3.json, "https://gist.githubusercontent.com/dougdowson/9832019/raw/ccd2f090db074655bed0c6084473421fb9df9da2/us.json") // Load US map
    .defer(d3.csv, "https://raw.githubusercontent.com/linhphaaaam/e14-final-nnbl/master/Data/opioid_death_rate.csv?token=ApiqSS7sEziN_j-k9zNg3q_CX1_oiC6Nks5cHNrrwA%3D%3D") // Load opioids death rates data
    .await(ready); // Run 'ready' when JSONs are loaded

function ready(error, us, data) {
  if (error) throw error;

  var states = topojson.feature(us, us.objects.states);

  // var rateById = {}; // create empty object for holding ataset

  data.forEach(function(d) {
    d.year = +d.year;
    d.id = +d.id;
    d.opioid_death_rate = +d.opioid_death_rate;
  });

  var dataByStateByYear = d3.nest()
    .key(function(d) { return d.id; })
    .key(function(d) { return d.year; })
    .map(data);

  states.features.forEach(function(state) {
    state.properties.years = dataByStateByYear[+state.id];
  });

  console.log(states.features);

  var color = d3.scale.threshold()
    .domain([0, 5, 10, 15, 20])
    .range(["#f2f0f7", "#dadaeb", "#bcbddc", "#9e9ac8", "#756bb1", "#54278f"]);

  var projection = d3.geo.albersUsa()
    .translate([width / 2, height / 2]);

  var path = d3.geo.path()
    .projection(projection);

  var svg = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  var stateShapes = svg.selectAll(".state")
    .data(states.features)
    .enter()
    .append('path')
      .attr('class', 'state')
      .attr('d', path)
      .attr('fill', function(d) {
        return color(d.properties.years[1999][0].opioid_death_rate)});
  console.log(stateShapes)

// legend

  var legend = svg.append("g")
    .attr("id", "legend");

  var legenditem = legend.selectAll(".legenditem")
    .data(d3.range(8))
    .enter()
    .append("g")
      .attr("class", "legenditem")
      .attr("transform", function(d, i) { return "translate(" + i * 31 + ",0)"; });

  legenditem.append("rect")
    .attr("x", width - 240)
    .attr("y", -7)
    .attr("width", 30)
    .attr("height", 6)
    .attr("class", "rect")
    .style("fill", function(d, i) { return legendColors[i]; });

  legenditem.append("text")
    .attr("x", width - 240)
    .attr("y", -10)
    .style("text-anchor", "middle")
    .text(function(d, i) { return legendText[i]; });

// slider update

  function update(year){
    slider.property("value", year);
    d3.select(".year").text(year);
    stateShapes.style("fill", function(d) {
      return color(d.properties.years[year][0].opioid_death_rate)
    });
  }

  var slider = d3.select(".slider")
    .append("input")
      .attr("type", "range")
      .attr("min", 1999)
      .attr("max", 2016)
      .attr("step", 1)
      .on("input", function() {
        var year = this.value;
        update(year);
  });

// update(1999);


  // svg.append("g")
  //     .attr("class", "states")
  //   .selectAll("path")
  //   .data(topojson.feature(us, us.objects.states).features)
  //   .enter().append("path")
  //     .attr("d", path)
  //     .style("stroke", "#4d0072");
}
