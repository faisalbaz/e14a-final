d3.json("/load_data", function (data) {

  data = data['users'];

  data.forEach(function(d){
    d.insurancetype = +d.insurancetype;
    d.state = +d.state;
    d.age = +d.age;
  })

  var svg = d3.select("#scatter");

      margin = {top: 20, right: 10, bottom: 50, left: 20},
      width = +svg.attr("width") - margin.left - margin.right,
      height = +svg.attr("height") - margin.top - margin.bottom,
      g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var xScale = d3.scaleLinear()
    .range([0, width]);

  var yScale = d3.scaleLinear()
    .range([height, 0]);

  var radius = d3.scaleSqrt()
    .range([2,5]);

  var xAxis = d3.axisBottom()
    .scale(xScale)
    .ticks(3);

  var yAxis = d3.axisLeft()
    .scale(yScale)
    .ticks(4);

  xScale.domain(d3.extent(data, function(d){
    return d.experience_yr;
  })).nice();

  yScale.domain(d3.extent(data, function(d){
    return d.hw1_hrs;
  })).nice();

  radius.domain(d3.extent(data, function(d){
    return d.age;
  })).nice();

  g.append('g')
    .attr('transform', 'translate(0,' + height + ')')
    .attr('class', 'x axis')
    .call(xAxis);

  g.append('g')
    .attr('transform', 'translate(0,0)')
    .attr('class', 'y axis')
    .call(yAxis);

  var bubble = g.selectAll('.bubble')
    .data(data)
    .enter().append('circle')
    .attr('class', 'bubble')
    .attr('cx', function(d){return xScale(d.experience_yr);})
    .attr('cy', function(d){ return yScale(d.hw1_hrs); })
    .attr('r', function(d){ return radius(d.age)*1.2; })
    .style('fill', '#1b7688');

  bubble.
        attr("transform", "translate(30,15)scale(0.85)");

  g.append('text')
    .attr("transform", "rotate(-90)")
    .attr('x', -90)
    .attr('y', 15)
    .attr('class', 'label')
    .text('State');

  g.append('text')
    .attr('x', (width/2) + 60)
    .attr('y', height + 35)
    .attr('text-anchor', 'end')
    .attr('class', 'label')
    .text('Insurance Type');

});
