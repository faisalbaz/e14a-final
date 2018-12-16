var data, txt, svg, x, y, bins, bar;
var formatCount = d3.format(",.0f");

d3.json("/load_data", function (error, json_data) {

  if(!error){
     data = json_data['users'];
     map = data.map(function(d,i){ return parseFloat(d.age); })
     createVis()
  }

  else{
    console.log("Data not loaded!!!")
  }

});
 
function createVis(){

  var total_users = data.length;

  txt = d3.select("#total_users_text")
    .append("text");

  txt  
    .text(total_users)
    .style("text-anchor", "start")
    .style("font-size", "30px")
    .style("font-style", "italic")
    .attr("fill", "#888")
    .attr("y", 440)
    .attr("x", 10);

  svg = d3.select("#barChart")
      margin = {top: 0, right: 45, bottom: 45, left: 0},
      width = +svg.attr("width") - margin.left - margin.right,
      height = +svg.attr("height") - margin.top - margin.bottom,
      g = svg.append("g")
             .attr("transform",
                   "translate(" + margin.left + "," + margin.top + ")");

  x = d3.scaleLinear()
      .rangeRound([0, width])
      .domain([d3.min(map), d3.max(map)]);

  bins = d3.histogram()
      .domain(x.domain())
      .thresholds(x.ticks(10))
      (map);

  y = d3.scaleLinear()
      .domain([0, d3.max(bins, function(d) {
        return d.length;
      })])
      .range([height, 50]);

  bar = g.selectAll(".bar")
      .data(bins)
      .enter()
      .append("g")
      .attr("class", "bar")
      .attr("transform", function(d) {
        return "translate(" + x(d.x0)*0.93 + "," + y(d.length) + ")";
      });

  bar
      .append("rect")
      .attr("fill", "#9b0a0a")
      .on("mouseover", function() {
            d3.select(this)
              .attr("fill", "red");
        })
      .on("mouseout", function(d, i) {
            d3.select(this)
              .transition()
              .duration(400)
              .attr("fill", "#9b0a0a");
          })
      .attr("x", 1)
      .attr("width", x(bins[0].x1) - x(bins[0].x0) - 1)
      .attr("height", function(d) { return height - y(d.length); });

  bar.append("text")
      .attr("dy", "-1em")
      .attr("y", 6)
      .attr("x", (x(bins[0].x1) - x(bins[0].x0)) / 2)
      .attr("text-anchor", "middle")
      .text(function(d) {
        return formatCount(d.length);
      });

  g.append("g")
      .attr("class", "axis axis--x")
      // .attr("transform", "translate(0," + (height-260) + ")")
      .attr("transform", "translate(0," + (height + 2) + ")")
      .call(d3.axisBottom(x).ticks(5));

  g.append('text')
    .attr('x', (width/2)+10)
    .attr('y', height + 35)
    .attr('text-anchor', 'end')
    .attr('class', 'label')
    .text('Age');

 }