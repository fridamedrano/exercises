
// Fireup the plugins
$(document).ready(function(){
	

});
/**
 * Handles toggling the navigation menu for small screens.
 */
( function() {
	var button = document.getElementById( 'topnav' ).getElementsByTagName( 'div' )[0],
	    menu   = document.getElementById( 'topnav' ).getElementsByTagName( 'ul' )[0];

	if ( undefined === button )
		return false;

	// Hide button if menu is missing or empty.
	if ( undefined === menu || ! menu.childNodes.length ) {
		button.style.display = 'none';
		return false;
	}

	button.onclick = function() {
		if ( -1 == menu.className.indexOf( 'srt-menu' ) )
			menu.className = 'srt-menu';

		if ( -1 != button.className.indexOf( 'toggled-on' ) ) {
			button.className = button.className.replace( ' toggled-on', '' );
			menu.className = menu.className.replace( ' toggled-on', '' );
		} else {
			button.className += ' toggled-on';
			menu.className += ' toggled-on';
		}
	};
} )();

/**
 *  Slide show code from: https://www.w3schools.com/howto/howto_js_slideshow.asp

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("slide");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; 
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1} 
    slides[slideIndex-1].style.display = "block"; 
    setTimeout(showSlides, 2000); // Change image every 2 seconds
}


/*start D3 Script*/


var w = 220,
    h = 400,
    t = .5,
    delta = .01,
    padding = 10,
    bezier = {},
    n = 4,
    stroke = d3.scale.category20b(),
		line = d3.svg.line().x(x).y(y),
    orders = d3.range(2, n + 2);

var points = [
  {x: 0, y: 346},
  {x: 160, y: 169},
  {x: 84,y: 42},
  {x: 0, y: 94},
  {x: 47, y: 160}
];

var vis = d3.select("#vis").selectAll("svg")
    .data(orders)
  .enter().append("svg")
    .attr("width", w + 2 * padding)
    .attr("height", h + 2 * padding)
  .append("g")
    .attr("transform", "translate(" + padding + "," + padding + ")");

update();

vis.selectAll("circle.control")
    .data(function(d) { return points.slice(0, d) })
  .enter().append("circle")
    .attr("class", "control")
    .attr("r", 7)
    .attr("cx", x)
    .attr("cy", y)
    .call(d3.behavior.drag()
      .on("dragstart", function(d) {
        this.__origin__ = [d.x, d.y];
				d3.select(this).classed("drag", true);
      })
      .on("drag", function(d) {
        d.x = Math.min(w, Math.max(0, this.__origin__[0] += d3.event.dx));
        d.y = Math.min(h, Math.max(0, this.__origin__[1] += d3.event.dy));
        bezier = {};
        update();
        vis.selectAll("circle.control")
          .attr("cx", x)
          .attr("cy", y);
      })
      .on("dragend", function() {
        delete this.__origin__;
				d3.select(this).classed("drag", false);
      }));

vis.append("text")
  .attr("class", "t")
  .attr("x", w / 2)
  .attr("y", h)
  .attr("text-anchor", "middle");

vis.selectAll("text.controltext")
    .data(function(d) { return points.slice(0, d); })
  .enter().append("text")
    .attr("class", "controltext")
    .attr("dx", "10px")
    .attr("dy", ".4em")
    .text(function(d, i) { return "P" + i });

var last = 0;
d3.timer(function(elapsed) {
  t = (t + (elapsed - last) / 5000) % 1;
  last = elapsed;
  update();
});

function update() {
  var interpolation = vis.selectAll("g")
      .data(function(d) { return getLevels(d, t); });
  interpolation.enter().append("g")
      .style("fill", colour)
      .style("stroke", colour);

  var circle = interpolation.selectAll("circle")
      .data(Object);
  circle.enter().append("circle")
      .attr("r", 4);
  circle
      .attr("cx", x)
      .attr("cy", y);

  var path = interpolation.selectAll("path")
      .data(function(d) { return [d]; });
  path.enter().append("path")
      .attr("class", "line")
      .attr("d", line);
  path.attr("d", line);

  var curve = vis.selectAll("path.curve")
      .data(getCurve);
  curve.enter().append("path")
      .attr("class", "curve");
  curve.attr("d", line);

  vis.selectAll("text.controltext")
      .attr("x", x)
      .attr("y", y);
  vis.selectAll("text.t")
      .text("t=" + t.toFixed(2));
}

function interpolate(d, p) {
  if (arguments.length < 2) p = t;
  var r = [];
  for (var i=1; i<d.length; i++) {
    var d0 = d[i-1], d1 = d[i];
    r.push({x: d0.x + (d1.x - d0.x) * p, y: d0.y + (d1.y - d0.y) * p});
  }
  return r;
}

function getLevels(d, t_) {
  if (arguments.length < 2) t_ = t;
  var x = [points.slice(0, d)];
  for (var i=1; i<d; i++) {
    x.push(interpolate(x[x.length-1], t_));
  }
  return x;
}

function getCurve(d) {
  var curve = bezier[d];
  if (!curve) {
    curve = bezier[d] = [];
    for (var t_=0; t_<=1; t_+=delta) {
      var x = getLevels(d, t_);
      curve.push(x[x.length-1][0]);
    }
  }
  return [curve.slice(0, t / delta + 1)];
}

function colour(d, i) {
  stroke(-i);
  return d.length > 1 ? stroke(i) : "red";
}

function x(d) { return d.x; }
function y(d) { return d.y; }


