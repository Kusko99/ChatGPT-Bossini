import java.io.FileInputStream;
import java.util.Properties;
import javax.swing.JOptionPane;
public class App {
    public static void main(String[] args) throws Exception {
        Properties properties = new Properties();
        properties.load(new FileInputStream("./app.properties"));
        String OPENAI_API_KEY = properties.getProperty("OPENAI_API_KEY");
        System.out.println(OPENAI_API_KEY);

        String assunto = "Java";
        String dificuldade = "Fácil";
        String tipo = "alternativa";
        ChatGPTClient client = new ChatGPTClient();
        String perguntaCriada =
        client.criarPergunta(OPENAI_API_KEY, assunto, tipo, dificuldade,
        tipo);
        JOptionPane.showMessageDialog(null, perguntaCriada);
    }   
}
