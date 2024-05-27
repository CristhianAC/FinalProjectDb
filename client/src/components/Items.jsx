import ItemCard from './ItemCard';

const Items = ({ items, addToCart }) => {
    return (
        <section className="productos-grid">
            {items.map((item, index) => (
                <ItemCard
                key={index}
                image={item.image}
                name={item.name}
                price={item.price}
                addToCart={() => addToCart(item)}
                />
            ))}
        </section>
    );
};

export default Items;
