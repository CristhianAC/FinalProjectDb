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
                addToCart={() => addToCart(item)}
                />
            ))}
        </section>
    );
};

export default Items;
