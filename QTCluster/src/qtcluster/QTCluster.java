/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package qtcluster;
import py4j.GatewayServer;
import edu.cornell.med.icb.clustering.MaxLinkageDistanceCalculator;
import edu.cornell.med.icb.clustering.QTClusterer;
import edu.cornell.med.icb.clustering.SimilarityDistanceCalculator;
import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author lagripe
 */
public class QTCluster {
    public static int qtCluster(float[][] matrix) {
        ArrayList<Float> list = new ArrayList<Float>();
        for (int i = 0; i < matrix.length; i++)
            for (int j = i + 1; j < matrix.length; j++)
                list.add(matrix[i][j]);
        final SimilarityDistanceCalculator distanceCalculator =
                new MaxLinkageDistanceCalculator() {
                    public double distance(final int i, final int j) {
                        return Double.parseDouble(""+list.get(i)) ;
                    }
                };
        int clusterSize = matrix.length * matrix[0].length;
        System.out.println(" clusterSize " + list.size() );
        final QTClusterer clusterer = new QTClusterer(list.size());
        final List<int[]> clusters = clusterer.cluster(distanceCalculator, (float) 0.05);
        
        int[] t ;
        for (int i = 0; i < clusters.size(); i++) {
                t = clusters.get(i);
                System.out.print(" { ");

                for (int j = 0; j < t.length; j++) {
                    System.out.print(t[j] + " ,");
                }    
                System.out.print(" } ");
                System.out.println();
        }
        
        return 0;
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
      return qtCluster(matrix);
   }
    public static void main(String[] args) {
        QTCluster app = new QTCluster();
    // app is now the gateway.entry_point
    GatewayServer server = new GatewayServer(app);
    server.start();
    }
    
}
