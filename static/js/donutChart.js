d3.json("/load_data", function (data) {

  data = data['users'];
  var drug_type_data = d3.nest()
  .key(function(d) { return d.drug_type; })
  .rollup(function(v) { return v.length; })
  .entries(data);

  var svg = d3.select("#donutChart").attr('class', 'pie');

      margin = {top: 10, right: 30, bottom: 30, left: 30},
      width = +svg.attr("width") - margin.left - margin.right,
      height = +svg.attr("height") - margin.top - margin.bottom,
      g = svg.append("g")
             .attr('transform', 'translate(' + (width/1.6) + ',' + (height/1.73) + ')');

  var text = "";

  var width = svg.attr("width");
  var height = svg.attr("height");
  var thickness = 50;
  var duration = 500;

  var radius = Math.min(width, height) / 2;
  var color = d3.scaleOrdinal()
  .domain(drug_type_data.keys())
  .range([
    '#1b7688',
    '#1b7676',
    '#f9d057',
    '#f29e2e',
    '#9b0a0a',
    '#d7191c',
    '#1b7678',//
    '#1b8876',
    '#f9d127',
    '#f29f2f',
    '#9b0a9a',
    '#d7182c'
  ]);

  var arc = d3.arc()
  .innerRadius(radius - thickness)
  .outerRadius(radius);

  var arcMouseOver = d3.arc()
  .innerRadius(radius - thickness -10)
  .outerRadius(radius);

  var pie = d3.pie()
  .value(function(d) {
    return d.value;
  })
  .sort(null);

  var path = g.selectAll('path')
  .data(pie(drug_type_data))
  .enter()
  .append("g")
    .on("mouseover", function(d) {
        let g = d3.select(this)
          .style("cursor", "pointer")
          .style("fill", "black")
          .append("g")
          .attr("class", "text-group");

        g.append("text")
          .attr("class", "name-text")
          .text(`${d.data.key}`)
          .attr('text-anchor', 'middle')
          .attr('dy', '-1.2em');

        g.append("text")
          .attr("class", "value-text")
          .text(`${Math.round(d.data.value/data.length*100)}%`)
          .attr('text-anchor', 'middle')
          .attr('dy', '.6em');
      })
    .on("mouseout", function(d) {
        d3.select(this)
          .style("cursor", "none")
          .style("fill", color(this._current))
          .select(".text-group").remove();
      })
    .append('path')
    .attr('d', arc)
    .attr('fill', (d,i) => color(i))
    .on("mouseover", function(d) {
        d3.select(this)
          .transition()
          .duration(400)
          .attr("d", arcMouseOver)
          .style("cursor", "pointer")
          .style("fill", "gray");
      })
    .on("mouseout", function(d) {
        d3.select(this)
          .transition()
          .duration(750)
          .attr("d", arc)
          .style("cursor", "none")
          .style("fill", color(this._current));
      })
    .each(function(d, i) {
      this._current = i;
    });

  g.append('text')
    .attr('text-anchor', 'middle')
    .attr('dy', '.35em')
    .text(text);

});
