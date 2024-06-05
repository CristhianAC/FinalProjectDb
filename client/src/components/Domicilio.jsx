







function Domicilio({ session }) {
  return (<section>
    {session ? <h1>¡Hola, {session.user.name}!</h1> : <h1>¡Hola!</h1>}
  </section>);
}

export default Domicilio;
