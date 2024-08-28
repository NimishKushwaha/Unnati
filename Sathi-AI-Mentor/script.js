window.gtranslateSettings = {
    default_language: "en",
    native_language_names: true,
    wrapper_selector: ".gtranslate_wrapper",
    switcher_horizontal_position: "right",
    switcher_vertical_position: "top",
    float_switcher_open_direction: "bottom",
  };
  
  const video = document.getElementById('bgVideo');
  
      document.addEventListener('click', function() {
        if (video.paused) {
          video.play();
        } else {
          video.pause();
        }
      });
  
  function toggleAbout() {
        var aboutContent = document.getElementById('aboutContent');
        aboutContent.style.maxHeight = (aboutContent.style.maxHeight === '0px' || aboutContent.style.maxHeight === '') ? '500px' : '0';
      }
  
  function scrolltoabout() {
    // Get the position of the aboutContent element
    var aboutContentPosition = document.getElementById('aboutContent').offsetTop;
  
    // Scroll smoothly to the aboutContent position
    window.scrollTo({
      top: aboutContentPosition,
      behavior: 'smooth'
      });
    }
    
    document.addEventListener('DOMContentLoaded', function() {
      // Add event listener for the Print link
      var printLink = document.getElementById('printLink'); // Update with the actual ID of your "PRINT" link
      if (printLink) {
        printLink.addEventListener('click', function() {
          printPage();
        });
      }
    });
    
    function printPage() {
      window.print();
    }