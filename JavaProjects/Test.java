import weka.core.converters.ConverterUtils.DataSource;

public class Test {
    public static void main(String[] args) {
        try {
            DataSource source = new DataSource("");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}