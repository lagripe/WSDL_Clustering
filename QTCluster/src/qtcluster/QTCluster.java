/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package qtcluster;
import py4j.GatewayServer;
/**
 *
 * @author lagripe
 */
public class QTCluster {
    public int addition(float[][] matrix) {
        return matrix.length;
      }
    public static int ParseMatrix(byte[] data) {
      java.nio.ByteBuffer buf = java.nio.ByteBuffer.wrap(data);
      int n = buf.getInt(), m = buf.getInt();
      float[][] matrix = new float[n][m];
      for (int i = 0; i < n; ++i)
         for (int j = 0; j < m; ++j)
            matrix[i][j] = buf.getFloat();
      for (int i = 0; i < n; i++){
         for (int j = 0; j < m; j++)
              System.out.print(matrix[i][j]+" ");
          System.out.println("");
      }
      return matrix.length;
   }
    public static void main(String[] args) {
        QTCluster app = new QTCluster();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
    }
    
}
