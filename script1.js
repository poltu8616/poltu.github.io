


  function convertToBold() {
      // Get the input text
      let inputText = document.getElementById('inputText').value;

      // Replace text wrapped in double asterisks with bold HTML tags
      let outputText = inputText.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');

      // Display the output text
      document.getElementById('outputText').innerHTML = outputText;

      // Ensure MathJax is triggered to render the content
      MathJax.typeset();
  }


