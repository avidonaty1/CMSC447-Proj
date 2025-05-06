// Print.jsx
import React, { useRef } from "react";
import { useReactToPrint } from "react-to-print";

const Print = () => {
  const componentRef = useRef();

  const handlePrint = useReactToPrint({
    content: () => componentRef.current,
  });

  return (
    <div>
      <button onClick={handlePrint}>Print</button>

      {/* This should be visible on the page */}
      <div ref={componentRef}>
        <h1>Hello, this should print!</h1>
      </div>
    </div>
  );
};

export default Print;
