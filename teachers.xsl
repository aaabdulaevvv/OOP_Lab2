<?xml version="1.0" encoding="UTF-8"?>
<xsl:transform version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <body>
        <h1>Teachers</h1>
            <table border="1">
                <tr bgcolor="#008000">
                    <th style="color:#FFFFFF">Name</th>
                    <th style="color:#FFFFFF">Faculty</th>
                    <th style="color:#FFFFFF">Department</th>
                    <th style="color:#FFFFFF">Material</th>
                    <th style="color:#FFFFFF">Material Type</th>
                    <th style="color:#FFFFFF">Number of Pages</th>
                    <th style="color:#FFFFFF">Date</th>
                </tr>
                <xsl:for-each select="teacherDataBase/teacher">
                <tr bgcolor="#FFFFFF">
                    <td><xsl:value-of select="@Name"/></td>
                    <td><xsl:value-of select="@Faculty"/></td>
                    <td><xsl:value-of select="@Department"/></td>
                    <td><xsl:value-of select="@Material"/></td>
                    <td><xsl:value-of select="@MaterialT"/></td>
                    <td><xsl:value-of select="@Extent"/></td>
                    <td><xsl:value-of select="@Date"/></td>
                </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:transform>