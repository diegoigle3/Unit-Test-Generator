public class ServicioUsuario {

    private UserRepository repository;
    private EmailNotifier notifier;
    private Encryptor encryptor;

    public ServicioUsuario(UserRepository repository, EmailNotifier notifier, Encryptor encryptor) {
        this.repository = repository;
        this.notifier = notifier;
        this.encryptor = encryptor;
    }

    public boolean registerUser(String username, String email, String password) {
        if (repository.existePorUsername(username)) {
            throw new IllegalArgumentException("The user already exists in the system.");
        }

        String hashPassword = encryptor.hash(password);
        Usuario nuevo = new Usuario(username, email, hashPassword);
        
        boolean guardado = repository.guardar(nuevo);
        
        if (guardado) {
            notifier.enviarMensajeBienvenida(email);
        }
        
        return guardado;
    }

    public void deleteUser(Long id) {
        Usuario usuario = repository.buscarPorId(id);
        if (usuario == null) {
            throw new RuntimeException("User not found.");
        }
        repository.eliminar(usuario);
        notifier.enviarMensajeDespedida(usuario.getEmail());
    }
    
    private void audit(String action) {//parser should ignore this method
        System.out.println("Auditing: " + action);
    }
}