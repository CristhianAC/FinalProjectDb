import React, { useEffect, useRef } from "react";

const Autocomplete = ({ onPlaceSelected }) => {
  const inputRef = useRef(null);

  useEffect(() => {
    const loadAutocomplete = () => {
      if (!inputRef.current) return;

      // Definir los límites para Barranquilla
      const bounds = new window.google.maps.LatLngBounds(
        new window.google.maps.LatLng(10.9413, -74.8324), // Suroeste de Barranquilla
        new window.google.maps.LatLng(11.084, -74.7616) // Noreste de Barranquilla
      );

      const autocomplete = new window.google.maps.places.Autocomplete(
        inputRef.current,
        {
          bounds: bounds,
          componentRestrictions: { country: "co" }, // Limitar a Colombia
          strictBounds: true,
          types: ["address"],
        }
      );

      autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        onPlaceSelected(place);
      });
    };

    if (window.google && window.google.maps && window.google.maps.places) {
      loadAutocomplete();
    } else {
      console.error("Google Maps JavaScript API library must be loaded.");
    }
  }, [onPlaceSelected]);

  return (
    <input
      ref={inputRef}
      type="text"
      className="border rounded-lg p-2 text-black"
      placeholder="Dirección de envío"
    />
  );
};

export default Autocomplete;
