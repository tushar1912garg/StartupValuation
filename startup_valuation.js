function calculateValuation() {
  var revenue = parseFloat(document.getElementById("revenue").value);
  var growthRate = parseFloat(document.getElementById("growthRate").value);
  var industryMultiplier = parseFloat(document.getElementById("industryMultiplier").value);
  var opportunityCost = parseFloat(document.getElementById("opportunityCost").value);
  var tam = parseFloat(document.getElementById("tam").value);
  var sam = parseFloat(document.getElementById("sam").value);
  var som = parseFloat(document.getElementById("som").value);

  var valuation = calculate_startup_valuation(revenue, growthRate, industryMultiplier, opportunityCost, tam, sam, som);

  if (valuation !== null) {
    document.getElementById("result").innerText = "The startup valuation is $" + valuation;
  } else {
    document.getElementById("result").innerText = "Invalid stage entered. Please choose 'idea', 'prototype', or 'revenue'.";
  }
}

function calculate_startup_valuation(revenue, growth_rate, industry_multiplier, opportunity_cost, tam, sam, som) {
  if (stage === 'idea') {
    return tam * 0.05;
  } else if (stage === 'prototype') {
    return tam * 0.1;
  } else if (stage === 'revenue') {
    var valuation = revenue * (1 + growth_rate) * industry_multiplier - opportunity_cost;
    return valuation * (sam / som);
  } else {
    return null;
  }
}
