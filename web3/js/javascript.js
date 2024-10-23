// Código existente

document.getElementById('property-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const name = document.getElementById('property-name').value;
    const purchasePrice = parseFloat(document.getElementById('purchase-price').value);
    const annualIncome = parseFloat(document.getElementById('annual-income').value);
    const annualExpenses = parseFloat(document.getElementById('annual-expenses').value);
  
    const profitability = ((annualIncome - annualExpenses) / purchasePrice) * 100;
  
    addToList(name, profitability);
  });
  
  function addToList(name, profitability) {
    const propertyList = document.getElementById('property-list');
    const listItem = document.createElement('li');
    listItem.textContent = `${name}: ${profitability.toFixed(2)}%`;
  
    // Inserción en la lista ordenada
    let inserted = false;
    for (let i = 0; i < propertyList.children.length; i++) {
      if (profitability > parseFloat(propertyList.children[i].dataset.profitability)) {
        propertyList.insertBefore(listItem, propertyList.children[i]);
        inserted = true;
        break;
      }
    }
  
    if (!inserted) {
      propertyList.appendChild(listItem);
    }
  
    listItem.dataset.profitability = profitability;
  }
  
  // Código para copiar al portapapeles
  document.getElementById('copy-button').addEventListener('click', function() {
    // Seleccionar la lista de inmuebles
    const propertyList = document.getElementById('property-list');
    
    // Crear un rango y seleccionarlo
    const range = document.createRange();
    range.selectNode(propertyList);
  
    // Seleccionar el rango
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
  
    try {
      // Copiar al portapapeles
      document.execCommand('copy');
      alert('Resultados copiados al portapapeles!');
    } catch (err) {
      alert('Error al copiar los resultados.');
    }
  
    // Deseleccionar el rango
    window.getSelection().removeAllRanges();
  });
  