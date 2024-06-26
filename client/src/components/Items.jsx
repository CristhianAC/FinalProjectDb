import ItemCard from './ItemCard';

const Items = ({ items, addToCart }) => {
  return (
    <section className="productos-grid">
      {items.map((item, index) => (
        <ItemCard
          key={index}
          image={item.imagen}
          name={item.nomproducto}
          price={item.precio}
          description={item.descrip}
          item={item}
          addToCart={addToCart}
          initialValue={item.cantidad} // Pasar initialValue aquí
        />
      ))}
    </section>
  );
};

export default Items;
