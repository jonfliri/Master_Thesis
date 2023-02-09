<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xi="http://www.w3.org/2001/XInclude">
  <xsl:template match="/">
    <html>
      <body>

        <h1>Package Name:
          <xsl:value-of select="AnyScriptPackage/Name"/>
        </h1>

        <xsl:call-template name="AllInTable"></xsl:call-template>


<!--
        <xsl:apply-templates select="AnyScriptPackage/SubPackage">
        </xsl:apply-templates>
-->

</body>
    </html>

  </xsl:template>

  <xsl:template match="SubPackage">
    <h2>
      Sub-Package: <xsl:value-of select="Name"/>
    </h2>
    <p>
      <xsl:value-of select="Description"/>
    </p>

    <table border="1">
      <tr valign="top">
        <td>File name:</td>
        <td>
          <xsl:value-of select="FileName"/>
        </td>
      </tr>
      <tr valign="top">
        <td>Dir:</td>
        <td>
          <xsl:value-of select="Dir"/>
        </td>
      </tr>
      <tr valign="top">
        <td>Format:</td>
        <td>
          <xsl:value-of select="Format"/>
        </td>
      </tr>
    </table>

    <table border="1">
      <xsl:for-each select="./*">
        <tr valign="top">
          <td>
            <xsl:value-of select="name()"/>
          </td>
          <td>
            <xsl:value-of select="."/>
          </td>
        </tr>

      </xsl:for-each>
    </table>

    <xsl:apply-templates select="AnyScriptApp">
    </xsl:apply-templates>

  </xsl:template>

  
  <xsl:template match="AnyScriptApp">

    <h3>
      Sub-Package: <xsl:value-of select="Name"/>
    </h3>
    <p>
      <xsl:value-of select="Description"/>
    </p>

    <xsl:call-template name="AllInTable"></xsl:call-template>
  </xsl:template>

  <xsl:template name="AllInTable">
    <table border="1">
      <xsl:for-each select="./*">
        <tr valign="top">
          <td>
            <xsl:value-of select="name()"/>
          </td>
          <td>
            <xsl:choose>
              <xsl:when test="count(*)=0">
                <xsl:value-of select="."/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:call-template name="AllInTable"></xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </td>
        </tr>

      </xsl:for-each>
    </table>

  </xsl:template>

</xsl:stylesheet>