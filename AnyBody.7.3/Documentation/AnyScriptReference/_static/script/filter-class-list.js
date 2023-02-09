

function filter_ul_list() {
    var input, filter, ul, li, a, i, txtValue;

    input = document.getElementById('multicolumn-toc-search');
    filter = input.value.toUpperCase();
    listelem = document.getElementsByClassName("multicolumn-toc")[0];
    li = listelem.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      txtValue = a.textContent || a.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
  }


  function filter_table() {
    const input = document.getElementById("filter-table-input");
    const inputStr = input.value.toUpperCase();
    table = document.getElementsByClassName("filter-table")[0];
    elemens = table.querySelectorAll('tr:not(:first-child)')
    elemens.forEach((tr) => {
      const anyMatch = [...tr.children]
        .some(td => td.textContent.toUpperCase().includes(inputStr));
      if (anyMatch) tr.style.removeProperty('display');
      else tr.style.display = 'none';
    });
  }

