const PriceFilter = ({ minPrice, maxPrice, setMinPrice, setMaxPrice }) => {
  return (
    <div className="price-filter">
      <label>
        Precio mínimo: {minPrice} COP
        <input
          type="range"
          min="0"
          max="50000"
          value={minPrice}
          onChange={(e) => setMinPrice(Number(e.target.value))}
        />
      </label>
      <label>
        Precio máximo: {maxPrice} COP
        <input
          type="range"
          min="0"
          max="50000"
          value={maxPrice}
          onChange={(e) => setMaxPrice(Number(e.target.value))}
        />
      </label>
    </div>
  );
};

export default PriceFilter;
