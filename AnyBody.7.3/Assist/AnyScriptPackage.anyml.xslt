<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:xi="http://www.w3.org/2001/XInclude"
xmlns:ab="http://www.anybodytech.com"
                >
<xsl:param name ="InstallPath">
  <xsl:value-of select="AnyScriptPackage/InstallPath"/>
</xsl:param>

<!--  <xsl:output
  method="xml|html|text|name"
  version="string"
  encoding="string"
  omit-xml-declaration="yes|no"
  standalone="yes|no"
  doctype-public="string"
  doctype-system="string"
  cdata-section-elements="namelist"
  indent="yes|no"
  media-type="string"/>
  -->
  <xsl:output
  method="xml"
  encoding="utf-8"
  indent="no"
  />

  <!-- Main -->
  <xsl:template match="/">
    <ab:anyml >

      <h2>
        <xsl:value-of select="AnyScriptPackage/Name"/>
      </h2>
      <!-- <xsl:value-of select="AnyScriptPackage/Description"/> 
      <xsl:copy-of select="AnyScriptPackage/Description"/>-->
      <xsl:copy-of select="AnyScriptPackage/Description/text() | AnyScriptPackage/Description/*"/>
      <br/>
      <br/>
      <ab:cmd>
        <xsl:attribute name="cmd">InstallDemoPackage <xsl:value-of select="AnyScriptPackage/ID"/> "<xsl:value-of select="$InstallPath"/>"</xsl:attribute>To re-install/update the installed demo files, follow this link.
      </ab:cmd>


      <xsl:apply-templates select="AnyScriptPackage/SubPackage"></xsl:apply-templates>
    </ab:anyml>
  </xsl:template>


  <!-- Sub-package template -->
  <xsl:template match="SubPackage">
    <xsl:if test="count(Name)">
      <h3>
        <xsl:value-of select="Name"/>
      </h3>
      <!--
      <xsl:if test="count(Description)">
        <xsl:copy-of select="Description/text() | Description/*"/>
      </xsl:if>
    -->

      <ab:os_explorer>
        <xsl:attribute name="file">
          <xsl:value-of select="$InstallPath"/>/<xsl:value-of select="RootPath"/>
        </xsl:attribute>
        To explore the installed demo files, follow this link.
      </ab:os_explorer>
    </xsl:if>

    <xsl:apply-templates select="AnyScriptApp">
      <xsl:with-param name="rootpath">
        <xsl:value-of select="RootPath"/>
      </xsl:with-param>
    </xsl:apply-templates>

  </xsl:template>

  <!-- AnyScript application template -->
  <xsl:template match="AnyScriptApp">
    <xsl:param name="rootpath">.</xsl:param>
    <xsl:if test="count(Name)">
      <!-- 
      <h4>
        <xsl:value-of select="Name"/>
      </h4>
      -->
      <br/>
      <br/>
      <b><xsl:value-of select="Name"/>: </b><br/>
      <xsl:if test="count(Description)">
        <!-- <xsl:value-of select="Description"/> -->
        <xsl:copy-of select="Description/text() | Description/*"/>
      </xsl:if>

      <br/>
      <em>Files: </em>
      <xsl:apply-templates select="AnyMainFile">
        <xsl:with-param name="rootpath">
          <xsl:value-of select="$rootpath"/>
        </xsl:with-param>
        <xsl:with-param name="modelpath">
          <xsl:value-of select="Path"/>
        </xsl:with-param>
      </xsl:apply-templates>
      <xsl:apply-templates select="File">
        <xsl:with-param name="rootpath">
          <xsl:value-of select="$rootpath"/>
        </xsl:with-param>
        <xsl:with-param name="modelpath">
          <xsl:value-of select="Path"/>
        </xsl:with-param>
      </xsl:apply-templates>
      <ab:os_explorer>
        <xsl:attribute name="file">
          <xsl:value-of select="$InstallPath"/>/<xsl:value-of select="$rootpath"/>/<xsl:value-of select="Path"/>
        </xsl:attribute>
        model-folder
      </ab:os_explorer>

    </xsl:if>

    <xsl:apply-templates select="AnyScriptApp"></xsl:apply-templates>

  </xsl:template>

  <!-- AnyMainFile template -->
  <xsl:template match="AnyMainFile">
    <xsl:param name="rootpath">.</xsl:param>
    <xsl:param name="modelpath">.</xsl:param>
    <ab:edt>
      <xsl:attribute name="file">
        <xsl:value-of select="$InstallPath"/>/<xsl:value-of select="$rootpath"/>/<xsl:value-of select="$modelpath"/>/<xsl:value-of select="."/>
      </xsl:attribute>
      <xsl:attribute name="line">0</xsl:attribute>
      <xsl:value-of select="."/>
    </ab:edt>
    <xsl:text>, </xsl:text>
  </xsl:template>

  <!-- AnyMainFile template -->
  <xsl:template match="File">
    <xsl:param name="rootpath">.</xsl:param>
    <xsl:param name="modelpath">.</xsl:param>
    <a>
      <xsl:attribute name="href">
        file://<xsl:value-of select="$InstallPath"/>/<xsl:value-of select="$rootpath"/>/<xsl:value-of select="$modelpath"/>/<xsl:value-of select="FileName"/>
      </xsl:attribute>
      <xsl:value-of select="FileName"/>
    </a>
    <xsl:text>, </xsl:text>
  </xsl:template>

</xsl:stylesheet>