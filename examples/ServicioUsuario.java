public class ServicioUsuario {

    private RepositorioUsuario repositorio;
    private NotificadorEmail notificador;
    private Encriptador encriptador;

    public ServicioUsuario(RepositorioUsuario repositorio, NotificadorEmail notificador, Encriptador encriptador) {
        this.repositorio = repositorio;
        this.notificador = notificador;
        this.encriptador = encriptador;
    }

    public boolean registrarUsuario(String username, String email, String password) {
        if (repositorio.existePorUsername(username)) {
            throw new IllegalArgumentException("El usuario ya existe en el sistema.");
        }

        String hashPassword = encriptador.hash(password);
        Usuario nuevo = new Usuario(username, email, hashPassword);
        
        boolean guardado = repositorio.guardar(nuevo);
        
        if (guardado) {
            notificador.enviarMensajeBienvenida(email);
        }
        
        return guardado;
    }

    public void darDeBaja(Long id) {
        Usuario usuario = repositorio.buscarPorId(id);
        if (usuario == null) {
            throw new RuntimeException("Usuario no encontrado.");
        }
        repositorio.eliminar(usuario);
        notificador.enviarMensajeDespedida(usuario.getEmail());
    }
    
    private void auditar(String accion) {//parser should ignore this method
        System.out.println("Auditando: " + accion);
    }
}