import com.google.gson.Gson;

public class TesteGSON {
    public static void main(String[] args) {
        RequisicaoChatGPT req = new RequisicaoChatGPT("text-davinci", "Por que o céu é azul?", 150);
        Gson gson = new Gson();
        String reqJSON = gson.toJson(req);
    }
}
