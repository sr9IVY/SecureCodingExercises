import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.sql.*;
import java.util.Base64;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.servlet.http.HttpServletRequest;

public class SecureLogin {

    // === Cryptographic Fix: Use PBKDF2 instead of MD5 ===
    public String hashPassword(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
        int iterations = 65536;
        int keyLength = 256;
        PBEKeySpec spec = new PBEKeySpec(password.toCharArray(), salt, iterations, keyLength);
        SecretKeyFactory skf = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] hash = skf.generateSecret(spec).getEncoded();
        return Base64.getEncoder().encodeToString(hash);
    }

    public byte[] generateSalt() {
        SecureRandom sr = new SecureRandom();
        byte[] salt = new byte[16];
        sr.nextBytes(salt);
        return salt;
    }

    // === Injection Fix: Use PreparedStatement ===
    public ResultSet getUserByUsername(Connection connection, HttpServletRequest request) throws SQLException {
        String username = request.getParameter("username");
        String query = "SELECT * FROM users WHERE username = ?";
        PreparedStatement pstmt = connection.prepareStatement(query);
        pstmt.setString(1, username);
        return pstmt.executeQuery();
    }

    // === Authentication Fix: Use hashed password comparison ===
    public boolean isAuthenticated(String inputPassword, String storedHash, byte[] storedSalt) throws NoSuchAlgorithmException, InvalidKeySpecException {
        String inputHash = hashPassword(inputPassword, storedSalt);
        return inputHash.equals(storedHash);
    }
}
