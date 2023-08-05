// The `Streamlit` object exists because our html file includes
// `streamlit-component-lib.js`.
// If you get an error about "Streamlit" not being defined, that
// means you're missing that file.

function sendValue(value) {
    Streamlit.setComponentValue(value)
  }
  
  /**
   * The component's render function. This will be called immediately after
   * the component is initially loaded, and then again every time the
   * component gets new data from Python.
   */
  function onRender(event) {
    // Only run the render code the first time the component is loaded.
    if (!window.rendered) {
      var protocol = "https";
      if (window.location.protocol == 'http:') {protocol = "http";}
      sendValue(protocol);
      window.rendered = true
    }
  }
  
  // Render the component whenever python send a "render event"
  Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
  // Tell Streamlit that the component is ready to receive events
  Streamlit.setComponentReady()
  // Don't actually need to display anything, so set the height to 0
  Streamlit.setFrameHeight(0)
  
